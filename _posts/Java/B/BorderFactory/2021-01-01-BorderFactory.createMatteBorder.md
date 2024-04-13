---
title: BorderFactory.createMatteBorder()
permalink: /Java/BorderFactory/createMatteBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createMatteBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MatteBorder createMatteBorder(int top, int left, int bottom, int right, Color color)
public static MatteBorder createMatteBorder(int top, int left, int bottom, int right, Icon tileIcon)
~~~

## Parámetros
* **int top**,  {% include w3api/param_description.html metodo=_dato parametro="int top" %}
* **int right**,  {% include w3api/param_description.html metodo=_dato parametro="int right" %}
* **Icon tileIcon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon tileIcon" %}
* **Color color**,  {% include w3api/param_description.html metodo=_dato parametro="Color color" %}
* **int left**,  {% include w3api/param_description.html metodo=_dato parametro="int left" %}
* **int bottom**,  {% include w3api/param_description.html metodo=_dato parametro="int bottom" %}

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

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
