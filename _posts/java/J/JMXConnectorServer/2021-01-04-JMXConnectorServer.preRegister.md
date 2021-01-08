---
title: JMXConnectorServer.preRegister()
permalink: Java/JMXConnectorServer/preRegister
date: 2021-01-04
key: JavaJava.J.JMXConnectorServer
category: java
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
* **MBeanServer mbs**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer mbs" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

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
{%- for _ldc in site.data.Java.J.JMXConnectorServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
