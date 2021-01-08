---
title: Container.add()
permalink: Java/Container/add
date: 2021-01-04
key: JavaJava.C.Container
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component add(Component comp)
public Component add(Component comp, int index)
public void add(Component comp, Object constraints)
public void add(Component comp, Object constraints, int index)
public Component add(String name, Component comp)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Component comp**,  {% include w3api/param_description.html metodo=_data parametro="Component comp" %}
* **Object constraints**,  {% include w3api/param_description.html metodo=_data parametro="Object constraints" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Container](/Java/Container/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Container.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
