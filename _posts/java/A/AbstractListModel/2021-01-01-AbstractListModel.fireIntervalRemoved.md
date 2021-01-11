---
title: AbstractListModel.fireIntervalRemoved()
permalink: Java/AbstractListModel/fireIntervalRemoved
date: 2021-01-11
key: JavaJava.A.AbstractListModel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractListModel.metodos valor="fireIntervalRemoved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireIntervalRemoved(Object source, int index0, int index1)
~~~

## Parámetros
* **int index1**,  {% include w3api/param_description.html metodo=_dato parametro="int index1" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **int index0**,  {% include w3api/param_description.html metodo=_dato parametro="int index0" %}

## Clase Padre
[AbstractListModel](/Java/AbstractListModel/)

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
