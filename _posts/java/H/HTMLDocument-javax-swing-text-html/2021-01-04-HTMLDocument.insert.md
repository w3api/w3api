---
title: HTMLDocument.insert()
permalink: Java/HTMLDocument-javax-swing-text-html/insert
date: 2021-01-04
key: JavaJava.H.HTMLDocument-javax-swing-text-html
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLDocument-javax-swing-text-html.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void insert(int offset, DefaultStyledDocument.ElementSpec[] data) throws BadLocationException
~~~

## Parámetros
* **DefaultStyledDocument.ElementSpec[] data**,  {% include w3api/param_description.html metodo=_data parametro="DefaultStyledDocument.ElementSpec[] data" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

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
