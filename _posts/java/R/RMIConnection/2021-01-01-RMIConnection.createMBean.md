---
title: RMIConnection.createMBean()
permalink: Java/RMIConnection/createMBean
date: 2021-01-11
key: Java.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="createMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectInstance createMBean(String className, ObjectName name, MarshalledObject params, String[] signature, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, IOException
ObjectInstance createMBean(String className, ObjectName name, ObjectName loaderName, MarshalledObject params, String[] signature, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, InstanceNotFoundException, IOException
ObjectInstance createMBean(String className, ObjectName name, ObjectName loaderName, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, InstanceNotFoundException, IOException
ObjectInstance createMBean(String className, ObjectName name, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, IOException
~~~

## Parámetros
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **MarshalledObject params**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject params" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="String[] signature" %}
* **ObjectName loaderName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName loaderName" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [SecurityException](/Java/SecurityException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [NotCompliantMBeanException](/Java/NotCompliantMBeanException/), [InstanceAlreadyExistsException](/Java/InstanceAlreadyExistsException/)

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
