---
title: HTMLWriter.textAreaContent()
permalink: /Java/HTMLWriter/textAreaContent/
date: 2021-01-11
key: Java.H.HTMLWriter
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLWriter.metodos valor="textAreaContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void textAreaContent(AttributeSet attr) throws BadLocationException, IOException
~~~

## Parámetros
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attr" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
