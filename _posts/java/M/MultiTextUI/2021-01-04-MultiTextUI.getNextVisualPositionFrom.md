---
title: MultiTextUI.getNextVisualPositionFrom()
permalink: Java/MultiTextUI/getNextVisualPositionFrom
date: 2021-01-04
key: JavaJava.M.MultiTextUI
category: java
tags: ['java se', 'javax.swing.plaf.multi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiTextUI.metodos valor="getNextVisualPositionFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getNextVisualPositionFrom(JTextComponent a, int b, Position.Bias c, int d, Position.Bias[] e) throws BadLocationException
~~~

## Parámetros
* **int d**,  {% include w3api/param_description.html metodo=_data parametro="int d" %}
* **Position.Bias c**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias c" %}
* **JTextComponent a**,  {% include w3api/param_description.html metodo=_data parametro="JTextComponent a" %}
* **Position.Bias[] e**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] e" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[MultiTextUI](/Java/MultiTextUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MultiTextUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
