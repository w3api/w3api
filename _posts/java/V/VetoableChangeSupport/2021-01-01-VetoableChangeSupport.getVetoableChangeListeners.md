---
title: VetoableChangeSupport.getVetoableChangeListeners()
permalink: /Java/VetoableChangeSupport/getVetoableChangeListeners/
date: 2021-01-11
key: Java.V.VetoableChangeSupport
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeSupport.metodos valor="getVetoableChangeListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VetoableChangeListener[] getVetoableChangeListeners()
public VetoableChangeListener[] getVetoableChangeListeners(String propertyName)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}

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
