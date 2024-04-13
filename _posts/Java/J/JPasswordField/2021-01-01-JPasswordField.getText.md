---
title: JPasswordField.getText()
permalink: /Java/JPasswordField/getText/
date: 2021-01-11
key: Java.J.JPasswordField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPasswordField.metodos valor="getText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public String getText()
@Deprecated public String getText(int offs, int len) throws BadLocationException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int offs**,  {% include w3api/param_description.html metodo=_dato parametro="int offs" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[JPasswordField](/Java/JPasswordField/)

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
