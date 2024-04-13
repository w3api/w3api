---
title: DirContext
permalink: /Java/DirContext/
date: 2021-01-11
key: Java.D.DirContext
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DirContext.description }}

## Sintaxis
~~~java
public interface DirContext extends Context
~~~

## Campos
* [ADD_ATTRIBUTE](/Java/DirContext/ADD_ATTRIBUTE/)
* [REMOVE_ATTRIBUTE](/Java/DirContext/REMOVE_ATTRIBUTE/)
* [REPLACE_ATTRIBUTE](/Java/DirContext/REPLACE_ATTRIBUTE/)

## Métodos
* [bind()](/Java/DirContext/bind/)
* [createSubcontext()](/Java/DirContext/createSubcontext/)
* [getAttributes()](/Java/DirContext/getAttributes/)
* [getSchema()](/Java/DirContext/getSchema/)
* [getSchemaClassDefinition()](/Java/DirContext/getSchemaClassDefinition/)
* [modifyAttributes()](/Java/DirContext/modifyAttributes/)
* [rebind()](/Java/DirContext/rebind/)
* [search()](/Java/DirContext/search/)

## Ejemplo
~~~java
{{ site.data.Java.D.DirContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
