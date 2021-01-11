---
title: VetoableChangeSupport.addVetoableChangeListener()
permalink: Java/VetoableChangeSupport/addVetoableChangeListener
date: 2021-01-11
key: JavaJava.V.VetoableChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeSupport.metodos valor="addVetoableChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addVetoableChangeListener(VetoableChangeListener listener)
public void addVetoableChangeListener(String propertyName, VetoableChangeListener listener)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **VetoableChangeListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="VetoableChangeListener listener" %}

## Clase Padre
[VetoableChangeSupport](/Java/VetoableChangeSupport/)

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
