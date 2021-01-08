---
title: SystemTray.removePropertyChangeListener()
permalink: Java/SystemTray/removePropertyChangeListener
date: 2021-01-04
key: JavaJava.S.SystemTray
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SystemTray.metodos valor="removePropertyChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removePropertyChangeListener(String propertyName, PropertyChangeListener listener)
~~~

## Parámetros
* **PropertyChangeListener listener**,  {% include w3api/param_description.html metodo=_data parametro="PropertyChangeListener listener" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}

## Clase Padre
[SystemTray](/Java/SystemTray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SystemTray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
