---
title: JTextComponent.getText()
permalink: Java/JTextComponent/getText
date: 2021-01-11
key: JavaJava.J.JTextComponent
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="getText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getText()
public String getText(int offs, int len) throws BadLocationException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int offs**,  {% include w3api/param_description.html metodo=_dato parametro="int offs" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

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
