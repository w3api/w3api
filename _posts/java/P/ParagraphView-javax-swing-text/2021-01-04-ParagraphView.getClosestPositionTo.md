---
title: ParagraphView.getClosestPositionTo()
permalink: Java/ParagraphView-javax-swing-text/getClosestPositionTo
date: 2021-01-04
key: JavaJava.P.ParagraphView-javax-swing-text
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParagraphView-javax-swing-text.metodos valor="getClosestPositionTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected int getClosestPositionTo(int pos, Position.Bias b, Shape a, int direction, Position.Bias[] biasRet, int rowIndex, int x) throws BadLocationException
~~~

## Parámetros
* **int rowIndex**,  {% include w3api/param_description.html metodo=_data parametro="int rowIndex" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] biasRet" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[ParagraphView](/Java/ParagraphView-javax-swing-text/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ParagraphView-javax-swing-text.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
