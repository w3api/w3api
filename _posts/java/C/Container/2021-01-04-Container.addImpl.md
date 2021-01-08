---
title: Container.addImpl()
permalink: Java/Container/addImpl
date: 2021-01-04
key: JavaJava.C.Container
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="addImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addImpl(Component comp, Object constraints, int index)
~~~

## Parámetros
* **Object constraints**,  {% include w3api/param_description.html metodo=_data parametro="Object constraints" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **Component comp**,  {% include w3api/param_description.html metodo=_data parametro="Component comp" %}

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
