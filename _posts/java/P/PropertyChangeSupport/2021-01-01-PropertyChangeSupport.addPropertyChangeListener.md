---
title: PropertyChangeSupport.addPropertyChangeListener()
permalink: /Java/PropertyChangeSupport/addPropertyChangeListener/
date: 2021-01-11
key: Java.P.PropertyChangeSupport
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeSupport.metodos valor="addPropertyChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addPropertyChangeListener(PropertyChangeListener listener)
public void addPropertyChangeListener(String propertyName, PropertyChangeListener listener)
~~~

## Parámetros
* **PropertyChangeListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeListener listener" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}

## Clase Padre
[PropertyChangeSupport](/Java/PropertyChangeSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
