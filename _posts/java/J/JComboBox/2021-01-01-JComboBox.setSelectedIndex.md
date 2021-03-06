---
title: JComboBox.setSelectedIndex()
permalink: /Java/JComboBox/setSelectedIndex/
date: 2021-01-11
key: Java.J.JComboBox
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.metodos valor="setSelectedIndex" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, preferred=true, description="The item at index is selected.") public void setSelectedIndex(int anIndex)
~~~

## Parámetros
* **int anIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int anIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JComboBox](/Java/JComboBox/)

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
