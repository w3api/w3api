---
title: VetoableChangeSupport.fireVetoableChange()
permalink: Java/VetoableChangeSupport/fireVetoableChange
date: 2021-01-04
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
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean oldValue" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_data parametro="int oldValue" %}
* **PropertyChangeEvent event**,  {% include w3api/param_description.html metodo=_data parametro="PropertyChangeEvent event" %}

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
{%- for _ldc in site.data.Java.V.VetoableChangeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
