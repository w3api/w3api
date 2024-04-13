---
title: AccessibleContext
permalink: /Java/AccessibleContext/
date: 2021-01-11
key: Java.A.AccessibleContext
category: Java
tags: ['java se', 'javax.accessibility', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AccessibleContext.description }}

## Sintaxis
~~~java
@JavaBean(description="Minimal information that all accessible objects return") public abstract class AccessibleContext extends Object
~~~

## Constructores
* [AccessibleContext()](/Java/AccessibleContext/AccessibleContext/)

## Campos
* [ACCESSIBLE_ACTION_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_ACTION_PROPERTY)
* [ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY)
* [ACCESSIBLE_CARET_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_CARET_PROPERTY)
* [ACCESSIBLE_CHILD_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_CHILD_PROPERTY)
* [ACCESSIBLE_COMPONENT_BOUNDS_CHANGED](/Java/AccessibleContext/ACCESSIBLE_COMPONENT_BOUNDS_CHANGED)
* [ACCESSIBLE_DESCRIPTION_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_DESCRIPTION_PROPERTY)
* [ACCESSIBLE_HYPERTEXT_OFFSET](/Java/AccessibleContext/ACCESSIBLE_HYPERTEXT_OFFSET)
* [ACCESSIBLE_INVALIDATE_CHILDREN](/Java/AccessibleContext/ACCESSIBLE_INVALIDATE_CHILDREN)
* [ACCESSIBLE_NAME_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_NAME_PROPERTY)
* [ACCESSIBLE_SELECTION_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_SELECTION_PROPERTY)
* [ACCESSIBLE_STATE_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_STATE_PROPERTY)
* [ACCESSIBLE_TABLE_CAPTION_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_CAPTION_CHANGED)
* [ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED)
* [ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED)
* [ACCESSIBLE_TABLE_MODEL_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_MODEL_CHANGED)
* [ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED)
* [ACCESSIBLE_TABLE_ROW_HEADER_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_ROW_HEADER_CHANGED)
* [ACCESSIBLE_TABLE_SUMMARY_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TABLE_SUMMARY_CHANGED)
* [ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED](/Java/AccessibleContext/ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED)
* [ACCESSIBLE_TEXT_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_TEXT_PROPERTY)
* [ACCESSIBLE_VALUE_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_VALUE_PROPERTY)
* [ACCESSIBLE_VISIBLE_DATA_PROPERTY](/Java/AccessibleContext/ACCESSIBLE_VISIBLE_DATA_PROPERTY)
* [accessibleDescription](/Java/AccessibleContext/accessibleDescription)
* [accessibleName](/Java/AccessibleContext/accessibleName)
* [accessibleParent](/Java/AccessibleContext/accessibleParent)

## Métodos
* [addPropertyChangeListener()](/Java/AccessibleContext/addPropertyChangeListener)
* [firePropertyChange()](/Java/AccessibleContext/firePropertyChange)
* [getAccessibleAction()](/Java/AccessibleContext/getAccessibleAction)
* [getAccessibleChild()](/Java/AccessibleContext/getAccessibleChild)
* [getAccessibleChildrenCount()](/Java/AccessibleContext/getAccessibleChildrenCount)
* [getAccessibleComponent()](/Java/AccessibleContext/getAccessibleComponent)
* [getAccessibleDescription()](/Java/AccessibleContext/getAccessibleDescription)
* [getAccessibleEditableText()](/Java/AccessibleContext/getAccessibleEditableText)
* [getAccessibleIcon()](/Java/AccessibleContext/getAccessibleIcon)
* [getAccessibleIndexInParent()](/Java/AccessibleContext/getAccessibleIndexInParent)
* [getAccessibleName()](/Java/AccessibleContext/getAccessibleName)
* [getAccessibleParent()](/Java/AccessibleContext/getAccessibleParent)
* [getAccessibleRelationSet()](/Java/AccessibleContext/getAccessibleRelationSet)
* [getAccessibleRole()](/Java/AccessibleContext/getAccessibleRole)
* [getAccessibleSelection()](/Java/AccessibleContext/getAccessibleSelection)
* [getAccessibleStateSet()](/Java/AccessibleContext/getAccessibleStateSet)
* [getAccessibleTable()](/Java/AccessibleContext/getAccessibleTable)
* [getAccessibleText()](/Java/AccessibleContext/getAccessibleText)
* [getAccessibleValue()](/Java/AccessibleContext/getAccessibleValue)
* [getLocale()](/Java/AccessibleContext/getLocale)
* [removePropertyChangeListener()](/Java/AccessibleContext/removePropertyChangeListener)
* [setAccessibleDescription()](/Java/AccessibleContext/setAccessibleDescription)
* [setAccessibleName()](/Java/AccessibleContext/setAccessibleName)
* [setAccessibleParent()](/Java/AccessibleContext/setAccessibleParent)

## Ejemplo
~~~java
{{ site.data.Java.A.AccessibleContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AccessibleContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
