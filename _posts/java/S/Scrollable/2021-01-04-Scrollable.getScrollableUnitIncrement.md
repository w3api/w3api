---
title: Scrollable.getScrollableUnitIncrement()
permalink: Java/Scrollable/getScrollableUnitIncrement
date: 2021-01-04
key: JavaJava.S.Scrollable
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Scrollable.metodos valor="getScrollableUnitIncrement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction)
~~~

## Parámetros
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_data parametro="int orientation" %}
* **Rectangle visibleRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle visibleRect" %}

## Clase Padre
[Scrollable](/Java/Scrollable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Scrollable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
