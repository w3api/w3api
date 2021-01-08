---
title: AppletInitializer.initialize()
permalink: Java/AppletInitializer/initialize
date: 2021-01-04
key: JavaJava.A.AppletInitializer
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AppletInitializer.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void initialize(Applet newAppletBean, BeanContext bCtxt)
~~~

## Parámetros
* **Applet newAppletBean**,  {% include w3api/param_description.html metodo=_data parametro="Applet newAppletBean" %}
* **BeanContext bCtxt**,  {% include w3api/param_description.html metodo=_data parametro="BeanContext bCtxt" %}

## Clase Padre
[AppletInitializer](/Java/AppletInitializer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AppletInitializer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
