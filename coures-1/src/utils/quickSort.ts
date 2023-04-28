import { Student } from "../app/studentSort";

export function quickSort(array: Student[]): Student[] {
  if (array.length <= 1) return array;
  let pivotIndex = Math.floor(array.length / 2); 
  let pivot = array[pivotIndex];
  let left: Student[] = []; 
  let right: Student[] = [];
  for (let i = 0; i < array.length; i++) {
    if (i === pivotIndex) continue;
    if (array[i] !== undefined && array[i].total !== undefined && array[i].total < pivot.total)
      left.push(array[i]);
    else right.push(array[i]);
  }
  return [...quickSort(left), pivot, ...quickSort(right)];  
}
