---
title: Component.firePropertyChange()
permalink: Java/Component/firePropertyChange
date: 2021-01-04
key: JavaJava.C.Component
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void firePropertyChange(String propertyName, boolean oldValue, boolean newValue)
public void firePropertyChange(String propertyName, byte oldValue, byte newValue)
public void firePropertyChange(String propertyName, char oldValue, char newValue)
public void firePropertyChange(String propertyName, double oldValue, double newValue)
public void firePropertyChange(String propertyName, float oldValue, float newValue)
protected void firePropertyChange(String propertyName, int oldValue, int newValue)
public void firePropertyChange(String propertyName, long oldValue, long newValue)
public void firePropertyChange(String propertyName, short oldValue, short newValue)
protected void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **byte oldValue**,  {% include w3api/param_description.html metodo=_data parametro="byte oldValue" %}
* **float oldValue**,  {% include w3api/param_description.html metodo=_data parametro="float oldValue" %}
* **long oldValue**,  {% include w3api/param_description.html metodo=_data parametro="long oldValue" %}
* **short oldValue**,  {% include w3api/param_description.html metodo=_data parametro="short oldValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **char oldValue**,  {% include w3api/param_description.html metodo=_data parametro="char oldValue" %}
* **byte newValue**,  {% include w3api/param_description.html metodo=_data parametro="byte newValue" %}
* **long newValue**,  {% include w3api/param_description.html metodo=_data parametro="long newValue" %}
* **float newValue**,  {% include w3api/param_description.html metodo=_data parametro="float newValue" %}
* **double newValue**,  {% include w3api/param_description.html metodo=_data parametro="double newValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean oldValue" %}
* **short newValue**,  {% include w3api/param_description.html metodo=_data parametro="short newValue" %}
* **char newValue**,  {% include w3api/param_description.html metodo=_data parametro="char newValue" %}
* **double oldValue**,  {% include w3api/param_description.html metodo=_data parametro="double oldValue" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_data parametro="int oldValue" %}

## Clase Padre
[Component](/Java/Component/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Component.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
