---
title: JColorChooser.setDragEnabled()
permalink: Java/JColorChooser/setDragEnabled
date: 2021-01-04
key: JavaJava.J.JColorChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JColorChooser.metodos valor="setDragEnabled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, description="Determines whether automatic drag handling is enabled.") public void setDragEnabled(boolean b)
~~~

## Parámetros
* **boolean b**,  {% include w3api/param_description.html metodo=_data parametro="boolean b" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[JColorChooser](/Java/JColorChooser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JColorChooser.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
