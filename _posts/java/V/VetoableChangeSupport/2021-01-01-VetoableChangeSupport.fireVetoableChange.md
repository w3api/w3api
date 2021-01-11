---
title: VetoableChangeSupport.fireVetoableChange()
permalink: Java/VetoableChangeSupport/fireVetoableChange
date: 2021-01-11
key: JavaJava.V.VetoableChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeSupport.metodos valor="fireVetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void fireVetoableChange(PropertyChangeEvent event) throws PropertyVetoException
public void fireVetoableChange(String propertyName, boolean oldValue, boolean newValue) throws PropertyVetoException
public void fireVetoableChange(String propertyName, int oldValue, int newValue) throws PropertyVetoException
public void fireVetoableChange(String propertyName, Object oldValue, Object newValue) throws PropertyVetoException
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **PropertyChangeEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeEvent event" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="int oldValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean oldValue" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

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
