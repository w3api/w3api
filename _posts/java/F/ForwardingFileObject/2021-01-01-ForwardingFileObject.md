---
title: ForwardingFileObject
permalink: /Java/ForwardingFileObject/
date: 2021-01-11
key: Java.F.ForwardingFileObject
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForwardingFileObject.description }}

## Sintaxis
~~~java
public class ForwardingFileObject<F extends FileObject> extends Object implements FileObject
~~~

## Constructores
* [ForwardingFileObject()](/Java/ForwardingFileObject/ForwardingFileObject/)

## Campos
* [fileObject](/Java/ForwardingFileObject/fileObject)

## Métodos
* [getCharContent()](/Java/ForwardingFileObject/getCharContent)
* [openInputStream()](/Java/ForwardingFileObject/openInputStream)
* [openOutputStream()](/Java/ForwardingFileObject/openOutputStream)
* [openReader()](/Java/ForwardingFileObject/openReader)
* [openWriter()](/Java/ForwardingFileObject/openWriter)

## Ejemplo
~~~java
{{ site.data.Java.F.ForwardingFileObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForwardingFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
