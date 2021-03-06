---
title: BasicGraphicsUtils.getClippedString()
permalink: /Java/BasicGraphicsUtils/getClippedString/
date: 2021-01-11
key: Java.B.BasicGraphicsUtils
category: Java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicGraphicsUtils.metodos valor="getClippedString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String getClippedString(JComponent c, FontMetrics fm, String string, int availTextWidth)
~~~

## Parámetros
* **int availTextWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int availTextWidth" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **FontMetrics fm**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics fm" %}
* **String string**,  {% include w3api/param_description.html metodo=_dato parametro="String string" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicGraphicsUtils](/Java/BasicGraphicsUtils/)

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
