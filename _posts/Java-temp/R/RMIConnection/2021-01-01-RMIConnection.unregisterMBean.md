---
title: RMIConnection.unregisterMBean()
permalink: /Java/RMIConnection/unregisterMBean/
date: 2021-01-11
key: Java.R.RMIConnection
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="unregisterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unregisterMBean(ObjectName name, Subject delegationSubject) throws InstanceNotFoundException, MBeanRegistrationException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [SecurityException](/Java/SecurityException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
