---
title: BoxLayout.addLayoutComponent()
permalink: /Java/BoxLayout/addLayoutComponent/
date: 2021-01-11
key: Java.B.BoxLayout
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BoxLayout.metodos valor="addLayoutComponent" %}

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

## Clase Padre
[BoxLayout](/Java/BoxLayout/)

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
