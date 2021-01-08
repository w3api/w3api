---
title: HTMLWriter.startTag()
permalink: Java/HTMLWriter/startTag
date: 2021-01-04
key: JavaJava.H.HTMLWriter
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLWriter.metodos valor="startTag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void startTag(Element elem) throws IOException, BadLocationException
~~~

## Parámetros
* **Element elem**,  {% include w3api/param_description.html metodo=_data parametro="Element elem" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLWriter](/Java/HTMLWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HTMLWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
