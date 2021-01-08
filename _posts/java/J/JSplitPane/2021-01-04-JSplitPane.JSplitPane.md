---
title: JSplitPane.JSplitPane()
permalink: Java/JSplitPane/JSplitPane
date: 2021-01-04
key: JavaJava.J.JSplitPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JSplitPane.constructores valor="JSplitPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JSplitPane()
@ConstructorProperties("orientation") public JSplitPane(int newOrientation)
public JSplitPane(int newOrientation, boolean newContinuousLayout)
public JSplitPane(int newOrientation, boolean newContinuousLayout, Component newLeftComponent, Component newRightComponent)
public JSplitPane(int newOrientation, Component newLeftComponent, Component newRightComponent)
~~~

## Parámetros
* **boolean newContinuousLayout**,  {% include w3api/param_description.html metodo=_data parametro="boolean newContinuousLayout" %}
* **int newOrientation**,  {% include w3api/param_description.html metodo=_data parametro="int newOrientation" %}
* **Component newLeftComponent**,  {% include w3api/param_description.html metodo=_data parametro="Component newLeftComponent" %}
* **Component newRightComponent**,  {% include w3api/param_description.html metodo=_data parametro="Component newRightComponent" %}

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
{%- for _ldc in site.data.Java.J.JSplitPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
