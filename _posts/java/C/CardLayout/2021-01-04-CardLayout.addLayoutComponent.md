---
title: CardLayout.addLayoutComponent()
permalink: Java/CardLayout/addLayoutComponent
date: 2021-01-04
key: JavaJava.C.CardLayout
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardLayout.metodos valor="addLayoutComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addLayoutComponent(Component comp, Object constraints)
@Deprecated public void addLayoutComponent(String name, Component comp)
~~~

## Parámetros
* **Object constraints**,  {% include w3api/param_description.html metodo=_data parametro="Object constraints" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Component comp**,  {% include w3api/param_description.html metodo=_data parametro="Component comp" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CardLayout](/Java/CardLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CardLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
