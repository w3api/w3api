---
title: HTMLEditorKit.insertHTML()
permalink: /Java/HTMLEditorKit/insertHTML/
date: 2021-01-11
key: Java.H.HTMLEditorKit
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLEditorKit.metodos valor="insertHTML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertHTML(HTMLDocument doc, int offset, String html, int popDepth, int pushDepth, HTML.Tag insertTag) throws BadLocationException, IOException
~~~

## Parámetros
* **HTML.Tag insertTag**,  {% include w3api/param_description.html metodo=_dato parametro="HTML.Tag insertTag" %}
* **HTMLDocument doc**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLDocument doc" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **String html**,  {% include w3api/param_description.html metodo=_dato parametro="String html" %}
* **int popDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int popDepth" %}
* **int pushDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int pushDepth" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLEditorKit](/Java/HTMLEditorKit/)

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
