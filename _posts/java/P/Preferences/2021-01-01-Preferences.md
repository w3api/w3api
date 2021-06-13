---
title: Preferences
permalink: /Java/Preferences/
date: 2021-01-11
key: Java.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Preferences.description }}

## Sintaxis
~~~java
public abstract class Preferences extends Object
~~~

## Constructores
* [Preferences()](/Java/Preferences/Preferences/)

## Campos
* [MAX_KEY_LENGTH](/Java/Preferences/MAX_KEY_LENGTH)
* [MAX_NAME_LENGTH](/Java/Preferences/MAX_NAME_LENGTH)
* [MAX_VALUE_LENGTH](/Java/Preferences/MAX_VALUE_LENGTH)

## Métodos
* [absolutePath()](/Java/Preferences/absolutePath)
* [addNodeChangeListener()](/Java/Preferences/addNodeChangeListener)
* [addPreferenceChangeListener()](/Java/Preferences/addPreferenceChangeListener)
* [childrenNames()](/Java/Preferences/childrenNames)
* [clear()](/Java/Preferences/clear)
* [exportNode()](/Java/Preferences/exportNode)
* [exportSubtree()](/Java/Preferences/exportSubtree)
* [flush()](/Java/Preferences/flush)
* [get()](/Java/Preferences/get)
* [getBoolean()](/Java/Preferences/getBoolean)
* [getByteArray()](/Java/Preferences/getByteArray)
* [getDouble()](/Java/Preferences/getDouble)
* [getFloat()](/Java/Preferences/getFloat)
* [getInt()](/Java/Preferences/getInt)
* [getLong()](/Java/Preferences/getLong)
* [importPreferences()](/Java/Preferences/importPreferences)
* [isUserNode()](/Java/Preferences/isUserNode)
* [keys()](/Java/Preferences/keys)
* [name()](/Java/Preferences/name)
* [node()](/Java/Preferences/node)
* [nodeExists()](/Java/Preferences/nodeExists)
* [parent()](/Java/Preferences/parent)
* [put()](/Java/Preferences/put)
* [putBoolean()](/Java/Preferences/putBoolean)
* [putByteArray()](/Java/Preferences/putByteArray)
* [putDouble()](/Java/Preferences/putDouble)
* [putFloat()](/Java/Preferences/putFloat)
* [putInt()](/Java/Preferences/putInt)
* [putLong()](/Java/Preferences/putLong)
* [remove()](/Java/Preferences/remove)
* [removeNode()](/Java/Preferences/removeNode)
* [removeNodeChangeListener()](/Java/Preferences/removeNodeChangeListener)
* [removePreferenceChangeListener()](/Java/Preferences/removePreferenceChangeListener)
* [sync()](/Java/Preferences/sync)
* [systemNodeForPackage()](/Java/Preferences/systemNodeForPackage)
* [systemRoot()](/Java/Preferences/systemRoot)
* [toString()](/Java/Preferences/toString)
* [userNodeForPackage()](/Java/Preferences/userNodeForPackage)
* [userRoot()](/Java/Preferences/userRoot)

## Ejemplo
~~~java
{{ site.data.Java.P.Preferences.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Preferences.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
