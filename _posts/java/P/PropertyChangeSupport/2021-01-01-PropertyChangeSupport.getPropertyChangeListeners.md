---
title: PropertyChangeSupport.getPropertyChangeListeners()
permalink: /Java/PropertyChangeSupport/getPropertyChangeListeners/
date: 2021-01-11
key: Java.P.PropertyChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeSupport.metodos valor="getPropertyChangeListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PropertyChangeListener[] getPropertyChangeListeners()
public PropertyChangeListener[] getPropertyChangeListeners(String propertyName)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}

## Clase Padre
[PropertyChangeSupport](/Java/PropertyChangeSupport/)

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
