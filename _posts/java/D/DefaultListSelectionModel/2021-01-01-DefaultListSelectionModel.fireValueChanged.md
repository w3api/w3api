---
title: DefaultListSelectionModel.fireValueChanged()
permalink: /Java/DefaultListSelectionModel/fireValueChanged/
date: 2021-01-11
key: Java.D.DefaultListSelectionModel
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultListSelectionModel.metodos valor="fireValueChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireValueChanged(boolean isAdjusting)
protected void fireValueChanged(int firstIndex, int lastIndex)
protected void fireValueChanged(int firstIndex, int lastIndex, boolean isAdjusting)
~~~

## Parámetros
* **boolean isAdjusting**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAdjusting" %}
* **int lastIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int lastIndex" %}
* **int firstIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int firstIndex" %}

## Clase Padre
[DefaultListSelectionModel](/Java/DefaultListSelectionModel/)

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
