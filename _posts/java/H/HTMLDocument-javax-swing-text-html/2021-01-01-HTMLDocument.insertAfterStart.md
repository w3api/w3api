---
title: HTMLDocument.insertAfterStart()
permalink: /Java/HTMLDocument-javax-swing-text-html/insertAfterStart/
date: 2021-01-11
key: Java.H.HTMLDocument-javax-swing-text-html
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLDocument-javax-swing-text-html.metodos valor="insertAfterStart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertAfterStart(Element elem, String htmlText) throws BadLocationException, IOException
~~~

## Parámetros
* **Element elem**,  {% include w3api/param_description.html metodo=_dato parametro="Element elem" %}
* **String htmlText**,  {% include w3api/param_description.html metodo=_dato parametro="String htmlText" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLDocument](/Java/HTMLDocument-javax-swing-text-html/)

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
