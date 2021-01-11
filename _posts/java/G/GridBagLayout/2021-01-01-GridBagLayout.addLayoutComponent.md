---
title: GridBagLayout.addLayoutComponent()
permalink: Java/GridBagLayout/addLayoutComponent
date: 2021-01-11
key: JavaJava.G.GridBagLayout
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GridBagLayout.metodos valor="addLayoutComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addLayoutComponent(Component comp, Object constraints)
public void addLayoutComponent(String name, Component comp)
~~~

## Parámetros
* **Object constraints**,  {% include w3api/param_description.html metodo=_dato parametro="Object constraints" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Component comp**,  {% include w3api/param_description.html metodo=_dato parametro="Component comp" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GridBagLayout](/Java/GridBagLayout/)

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
