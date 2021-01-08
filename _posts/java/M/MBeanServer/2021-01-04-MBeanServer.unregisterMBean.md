---
title: MBeanServer.unregisterMBean()
permalink: Java/MBeanServer/unregisterMBean
date: 2021-01-04
key: JavaJava.M.MBeanServer
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="unregisterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unregisterMBean(ObjectName name) throws InstanceNotFoundException, MBeanRegistrationException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[MBeanRegistrationException](/Java/MBeanRegistrationException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [RuntimeErrorException](/Java/RuntimeErrorException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
