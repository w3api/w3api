---
title: Container.remove()
permalink: /Java/Container/remove/
date: 2021-01-11
key: Java.C.Container
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(int index)
public void remove(Component comp)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **Component comp**,  {% include w3api/param_description.html metodo=_dato parametro="Component comp" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Container](/Java/Container/)

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
