---
title: JTextArea.getLineOfOffset()
permalink: /Java/JTextArea/getLineOfOffset/
date: 2021-01-11
key: Java.J.JTextArea
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.metodos valor="getLineOfOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getLineOfOffset(int offset) throws BadLocationException
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[JTextArea](/Java/JTextArea/)

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
