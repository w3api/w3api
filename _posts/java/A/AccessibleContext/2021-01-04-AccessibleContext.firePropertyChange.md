---
title: AccessibleContext.firePropertyChange()
permalink: Java/AccessibleContext/firePropertyChange
date: 2021-01-04
key: JavaJava.A.AccessibleContext
category: java
tags: ['java se', 'javax.accessibility', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessibleContext.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}

## Clase Padre
[AccessibleContext](/Java/AccessibleContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AccessibleContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
