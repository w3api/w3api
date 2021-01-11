---
title: BasicGraphicsUtils.getStringWidth()
permalink: Java/BasicGraphicsUtils/getStringWidth
date: 2021-01-11
key: JavaJava.B.BasicGraphicsUtils
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicGraphicsUtils.metodos valor="getStringWidth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static float getStringWidth(JComponent c, FontMetrics fm, String string)
~~~

## Parámetros
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
