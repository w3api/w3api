---
title: SwingWorker.firePropertyChange()
permalink: /Java/SwingWorker/firePropertyChange/
date: 2021-01-11
key: Java.S.SwingWorker
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingWorker.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}

## Clase Padre
[SwingWorker](/Java/SwingWorker/)

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
