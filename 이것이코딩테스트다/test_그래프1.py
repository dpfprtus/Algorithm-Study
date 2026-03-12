import os
import importlib.util

# Dynamically import the target module due to non-standard characters in the filename
current_dir = os.path.dirname(os.path.abspath(__file__))
module_name = '그래프1'
file_path = os.path.join(current_dir, f'{module_name}.py')

spec = importlib.util.spec_from_file_location(module_name, file_path)
graph1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(graph1)

find_parent = graph1.find_parent
union_parent = graph1.union_parent

def test_initialization():
    """Test initial state of disjoint set array."""
    n = 4
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    # Each node should be its own parent initially
    assert parent == [0, 1, 2, 3, 4]
    for i in range(1, n + 1):
        assert find_parent(parent, i) == i

def test_union_parent_basic():
    """Test that union_parent correctly merges two sets."""
    n = 4
    parent = [0, 1, 2, 3, 4]

    # Merge 1 and 2
    union_parent(parent, 1, 2)
    # The smaller root (1) should become the parent of the larger root (2)
    assert parent[2] == 1
    assert find_parent(parent, 1) == 1
    assert find_parent(parent, 2) == 1

def test_union_parent_larger_first():
    """Test that union_parent works when the first argument is the larger root."""
    n = 4
    parent = [0, 1, 2, 3, 4]

    # Merge 3 and 1
    union_parent(parent, 3, 1)
    # The smaller root (1) should become the parent of the larger root (3)
    assert parent[3] == 1
    assert find_parent(parent, 1) == 1
    assert find_parent(parent, 3) == 1

def test_find_parent_path_compression():
    """Test that find_parent performs path compression."""
    # Create a linear tree: 1 <- 2 <- 3 <- 4
    parent = [0, 1, 1, 2, 3]

    # Finding parent of 4 should return 1 and compress the path
    root = find_parent(parent, 4)
    assert root == 1

    # Check that path compression occurred
    assert parent[4] == 1
    assert parent[3] == 1  # 3 was compressed as part of the recursive calls
    assert parent[2] == 1

def test_multiple_unions():
    """Test multiple union operations and verifying final state."""
    n = 6
    parent = [0, 1, 2, 3, 4, 5, 6]

    union_parent(parent, 1, 4) # parent[4] = 1
    union_parent(parent, 2, 3) # parent[3] = 2
    union_parent(parent, 2, 4) # 4's root is 1, 2's root is 2. So parent[2] = 1
    union_parent(parent, 5, 6) # parent[6] = 5

    assert find_parent(parent, 1) == 1
    assert find_parent(parent, 2) == 1
    assert find_parent(parent, 3) == 1
    assert find_parent(parent, 4) == 1

    assert find_parent(parent, 5) == 5
    assert find_parent(parent, 6) == 5

    # Check that 1-4 and 5-6 are separate sets
    assert find_parent(parent, 4) != find_parent(parent, 6)
