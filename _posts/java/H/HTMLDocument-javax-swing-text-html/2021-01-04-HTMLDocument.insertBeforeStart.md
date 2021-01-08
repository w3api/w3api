---
title: HTMLDocument.insertBeforeStart()
permalink: Java/HTMLDocument-javax-swing-text-html/insertBeforeStart
date: 2021-01-04
key: JavaJava.H.HTMLDocument-javax-swing-text-html
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLDocument-javax-swing-text-html.metodos valor="insertBeforeStart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertBeforeStart(Element elem, String htmlText) throws BadLocationException, IOException
~~~

## Parámetros
* **String htmlText**,  {% include w3api/param_description.html metodo=_data parametro="String htmlText" %}
* **Element elem**,  {% include w3api/param_description.html metodo=_data parametro="Element elem" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLDocument](/Java/HTMLDocument-javax-swing-text-html/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HTMLDocument-javax-swing-text-html.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
