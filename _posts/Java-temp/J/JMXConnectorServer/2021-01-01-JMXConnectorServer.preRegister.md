---
title: JMXConnectorServer.preRegister()
permalink: /Java/JMXConnectorServer/preRegister/
date: 2021-01-11
key: Java.J.JMXConnectorServer
category: Java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorServer.metodos valor="preRegister" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectName preRegister(MBeanServer mbs, ObjectName name)
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **MBeanServer mbs**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer mbs" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnectorServer](/Java/JMXConnectorServer/)

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
