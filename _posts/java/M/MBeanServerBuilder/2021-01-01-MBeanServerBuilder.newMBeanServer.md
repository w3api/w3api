---
title: MBeanServerBuilder.newMBeanServer()
permalink: /Java/MBeanServerBuilder/newMBeanServer/
date: 2021-01-11
key: Java.M.MBeanServerBuilder
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerBuilder.metodos valor="newMBeanServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanServer newMBeanServer(String defaultDomain, MBeanServer outer, MBeanServerDelegate delegate)
~~~

## Parámetros
* **String defaultDomain**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultDomain" %}
* **MBeanServerDelegate delegate**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServerDelegate delegate" %}
* **MBeanServer outer**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer outer" %}

## Clase Padre
[MBeanServerBuilder](/Java/MBeanServerBuilder/)

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
