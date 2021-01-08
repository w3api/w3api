---
title: MBeanServerBuilder.newMBeanServer()
permalink: Java/MBeanServerBuilder/newMBeanServer
date: 2021-01-04
key: JavaJava.M.MBeanServerBuilder
category: java
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
* **MBeanServerDelegate delegate**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServerDelegate delegate" %}
* **MBeanServer outer**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer outer" %}
* **String defaultDomain**,  {% include w3api/param_description.html metodo=_data parametro="String defaultDomain" %}

## Clase Padre
[MBeanServerBuilder](/Java/MBeanServerBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
