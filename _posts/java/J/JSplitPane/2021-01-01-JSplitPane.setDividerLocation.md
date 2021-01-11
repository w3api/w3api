---
title: JSplitPane.setDividerLocation()
permalink: Java/JSplitPane/setDividerLocation
date: 2021-01-11
key: JavaJava.J.JSplitPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JSplitPane.metodos valor="setDividerLocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="The location of the divider.") public void setDividerLocation(double proportionalLocation)
@BeanProperty(description="The location of the divider.") public void setDividerLocation(int location)
~~~

## Parámetros
* **int location**,  {% include w3api/param_description.html metodo=_dato parametro="int location" %}
* **double proportionalLocation**,  {% include w3api/param_description.html metodo=_dato parametro="double proportionalLocation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JSplitPane](/Java/JSplitPane/)

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
