---
title: HTMLDocument.getReader()
permalink: Java/HTMLDocument-javax-swing-text-html/getReader
date: 2021-01-11
key: JavaJava.H.HTMLDocument-javax-swing-text-html
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLDocument-javax-swing-text-html.metodos valor="getReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HTMLEditorKit.ParserCallback getReader(int pos)
public HTMLEditorKit.ParserCallback getReader(int pos, int popDepth, int pushDepth, HTML.Tag insertTag)
~~~

## Parámetros
* **int popDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int popDepth" %}
* **int pushDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int pushDepth" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}
* **HTML.Tag insertTag**,  {% include w3api/param_description.html metodo=_dato parametro="HTML.Tag insertTag" %}

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