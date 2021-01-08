---
title: NavigationFilter.getNextVisualPositionFrom()
permalink: Java/NavigationFilter/getNextVisualPositionFrom
date: 2021-01-04
key: JavaJava.N.NavigationFilter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigationFilter.metodos valor="getNextVisualPositionFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getNextVisualPositionFrom(JTextComponent text, int pos, Position.Bias bias, int direction, Position.Bias[] biasRet) throws BadLocationException
~~~

## Parámetros
* **JTextComponent text**,  {% include w3api/param_description.html metodo=_data parametro="JTextComponent text" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] biasRet" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}
* **Position.Bias bias**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias bias" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NavigationFilter](/Java/NavigationFilter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NavigationFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
