---
title: MatteBorder.MatteBorder()
permalink: Java/MatteBorder/MatteBorder
date: 2021-01-04
key: JavaJava.M.MatteBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MatteBorder.constructores valor="MatteBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MatteBorder(int top, int left, int bottom, int right, Color matteColor)
public MatteBorder(int top, int left, int bottom, int right, Icon tileIcon)
public MatteBorder(Insets borderInsets, Color matteColor)
public MatteBorder(Insets borderInsets, Icon tileIcon)
public MatteBorder(Icon tileIcon)
~~~

## Parámetros
* **int left**,  {% include w3api/param_description.html metodo=_data parametro="int left" %}
* **Insets borderInsets**,  {% include w3api/param_description.html metodo=_data parametro="Insets borderInsets" %}
* **int top**,  {% include w3api/param_description.html metodo=_data parametro="int top" %}
* **Color matteColor**,  {% include w3api/param_description.html metodo=_data parametro="Color matteColor" %}
* **Icon tileIcon**,  {% include w3api/param_description.html metodo=_data parametro="Icon tileIcon" %}
* **int right**,  {% include w3api/param_description.html metodo=_data parametro="int right" %}
* **int bottom**,  {% include w3api/param_description.html metodo=_data parametro="int bottom" %}

## Clase Padre
[MatteBorder](/Java/MatteBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MatteBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
